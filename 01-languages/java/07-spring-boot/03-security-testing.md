# Spring Boot Security & Testing
*JWT auth, exception handling, and testing*

## Exception Handling
*Global error responses*

```java
@RestControllerAdvice
public class GlobalExceptionHandler {

    @ExceptionHandler(ResourceNotFoundException.class)
    @ResponseStatus(HttpStatus.NOT_FOUND)
    public Map<String, String> handleNotFound(ResourceNotFoundException ex) {
        return Map.of("error", ex.getMessage());
    }

    @ExceptionHandler(MethodArgumentNotValidException.class)
    @ResponseStatus(HttpStatus.BAD_REQUEST)
    public Map<String, Object> handleValidation(MethodArgumentNotValidException ex) {
        Map<String, String> errors = new HashMap<>();
        ex.getBindingResult().getFieldErrors()
          .forEach(e -> errors.put(e.getField(), e.getDefaultMessage()));
        return Map.of("errors", errors);
    }
}
```

---

## Spring Security + JWT
*Protect endpoints with JWT tokens*

```bash
# pom.xml dependency
# spring-boot-starter-security
# io.jsonwebtoken:jjwt-api:0.11.5
# io.jsonwebtoken:jjwt-impl:0.11.5
```

```java
@Component
public class JwtFilter extends OncePerRequestFilter {

    @Override
    protected void doFilterInternal(HttpServletRequest req,
                                    HttpServletResponse res,
                                    FilterChain chain) throws ServletException, IOException {
        String header = req.getHeader("Authorization");
        if (header != null && header.startsWith("Bearer ")) {
            String token = header.substring(7);
            String userId = jwtService.extractUserId(token);
            if (userId != null) {
                var auth = new UsernamePasswordAuthenticationToken(userId, null, List.of());
                SecurityContextHolder.getContext().setAuthentication(auth);
            }
        }
        chain.doFilter(req, res);
    }
}

// SecurityConfig
@Bean
public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
    return http
        .csrf(csrf -> csrf.disable())
        .sessionManagement(s -> s.sessionCreationPolicy(STATELESS))
        .authorizeHttpRequests(auth -> auth
            .requestMatchers("/api/auth/**").permitAll()
            .anyRequest().authenticated()
        )
        .addFilterBefore(jwtFilter, UsernamePasswordAuthenticationFilter.class)
        .build();
}
```

---

## Testing with MockMvc
*Test controllers without starting server*

```java
@WebMvcTest(UserController.class)
class UserControllerTest {

    @Autowired MockMvc mockMvc;
    @MockBean UserService userService;
    @Autowired ObjectMapper objectMapper;

    @Test
    void getUsers_returnsOk() throws Exception {
        when(userService.getAll()).thenReturn(List.of(
            new User(1L, "Alice", "alice@a.com")
        ));

        mockMvc.perform(get("/api/users"))
            .andExpect(status().isOk())
            .andExpect(jsonPath("$[0].name").value("Alice"));
    }

    @Test
    void createUser_invalidEmail_returns400() throws Exception {
        var req = new UserRequest("Alice", "not-an-email");
        mockMvc.perform(post("/api/users")
                .contentType(MediaType.APPLICATION_JSON)
                .content(objectMapper.writeValueAsString(req)))
            .andExpect(status().isBadRequest());
    }
}
```

---

## Integration Test
*Full stack with embedded DB*

```java
@SpringBootTest
@AutoConfigureMockMvc
@Transactional
class UserIntegrationTest {

    @Autowired MockMvc mockMvc;
    @Autowired UserRepository userRepository;

    @Test
    void createAndGetUser() throws Exception {
        var req = new UserRequest("Alice", "alice@example.com");

        mockMvc.perform(post("/api/users")
                .contentType(MediaType.APPLICATION_JSON)
                .content("""{"name":"Alice","email":"alice@example.com"}"""))
            .andExpect(status().isCreated())
            .andExpect(jsonPath("$.id").exists());

        assertEquals(1, userRepository.count());
    }
}
```
