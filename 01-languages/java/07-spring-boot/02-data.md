# Spring Boot Data
*JPA, Hibernate, and database access*

## Spring Data JPA
*ORM with repository pattern*

**JPA (Jakarta Persistence API)** – Standard ORM specification for Java  
**Hibernate** – JPA implementation used by Spring Boot by default  
**Entity** – Java class mapped to a DB table  
**Repository** – Interface with auto-generated DB queries  

---

## Entity
*Map a class to a table*

```java
import jakarta.persistence.*;
import lombok.Data;
import lombok.NoArgsConstructor;

@Entity
@Table(name = "users")
@Data
@NoArgsConstructor
public class User {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(nullable = false)
    private String name;

    @Column(unique = true, nullable = false)
    private String email;

    @CreationTimestamp
    private LocalDateTime createdAt;
}
```

---

## Repository
*Auto-generated CRUD operations*

```java
import org.springframework.data.jpa.repository.JpaRepository;
import java.util.Optional;

public interface UserRepository extends JpaRepository<User, Long> {
    // Auto-generated: findById, findAll, save, delete, count, existsById

    // Derived queries from method names:
    Optional<User> findByEmail(String email);
    List<User> findByNameContainingIgnoreCase(String name);
    boolean existsByEmail(String email);

    // Custom JPQL query
    @Query("SELECT u FROM User u WHERE u.createdAt > :since")
    List<User> findRecentUsers(@Param("since") LocalDateTime since);
}
```

---

## Service Layer
*Business logic using repository*

```java
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;
import lombok.RequiredArgsConstructor;

@Service
@RequiredArgsConstructor
public class UserService {

    private final UserRepository userRepository;

    public List<User> getAll() {
        return userRepository.findAll();
    }

    public User getById(Long id) {
        return userRepository.findById(id)
            .orElseThrow(() -> new ResourceNotFoundException("User not found: " + id));
    }

    @Transactional
    public User create(UserRequest req) {
        if (userRepository.existsByEmail(req.email())) {
            throw new ConflictException("Email already in use");
        }
        User user = new User();
        user.setName(req.name());
        user.setEmail(req.email());
        return userRepository.save(user);
    }

    @Transactional
    public void delete(Long id) {
        User user = getById(id);
        userRepository.delete(user);
    }
}
```

---

## DTO Pattern
*Separate API shape from DB shape*

```java
// Request DTO (record = immutable POJO)
public record UserRequest(
    @NotBlank String name,
    @Email @NotBlank String email
) {}

// Response DTO
public record UserResponse(Long id, String name, String email) {
    public static UserResponse from(User user) {
        return new UserResponse(user.getId(), user.getName(), user.getEmail());
    }
}

// In controller
@PostMapping
@ResponseStatus(HttpStatus.CREATED)
public UserResponse create(@Valid @RequestBody UserRequest req) {
    return UserResponse.from(userService.create(req));
}
```

**Rule**: never return JPA entities directly from controllers — expose DTOs only.
