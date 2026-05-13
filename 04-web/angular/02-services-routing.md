# Angular Services & Routing
*Dependency injection, HTTP, and navigation*

## Services and Dependency Injection
*Shared logic injected into components*

```typescript
// users.service.ts
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({ providedIn: 'root' })   // singleton across app
export class UsersService {
  private url = '/api/users';

  constructor(private http: HttpClient) {}

  getAll(): Observable<User[]> {
    return this.http.get<User[]>(this.url);
  }

  create(user: Partial<User>): Observable<User> {
    return this.http.post<User>(this.url, user);
  }

  delete(id: number): Observable<void> {
    return this.http.delete<void>(`${this.url}/${id}`);
  }
}
```

```typescript
// users.component.ts — inject and use service
constructor(private usersService: UsersService) {}

ngOnInit(): void {
  this.usersService.getAll().subscribe(users => {
    this.users = users;
  });
}
```

---

## HttpClient Setup
*Configure HTTP module*

```typescript
// app.module.ts
import { HttpClientModule } from '@angular/common/http';

@NgModule({
  imports: [HttpClientModule]
})
export class AppModule {}
```

---

## Routing
*Navigation between views*

```typescript
// app-routing.module.ts
import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { UsersComponent } from './users/users.component';
import { UserDetailComponent } from './user-detail/user-detail.component';

const routes: Routes = [
  { path: '',          redirectTo: '/users', pathMatch: 'full' },
  { path: 'users',     component: UsersComponent },
  { path: 'users/:id', component: UserDetailComponent },
  { path: '**',        redirectTo: '/users' }   // wildcard
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {}
```

```html
<!-- app.component.html -->
<nav>
  <a routerLink="/users" routerLinkActive="active">Users</a>
</nav>
<router-outlet></router-outlet>   <!-- render matched component here -->
```

---

## Route Params
*Read URL parameters in component*

```typescript
import { ActivatedRoute } from '@angular/router';

constructor(
  private route: ActivatedRoute,
  private usersService: UsersService
) {}

ngOnInit(): void {
  const id = Number(this.route.snapshot.paramMap.get('id'));
  this.usersService.getById(id).subscribe(u => this.user = u);
}
```

---

## Route Guards
*Protect routes from unauthorized access*

```typescript
// auth.guard.ts
import { Injectable } from '@angular/core';
import { CanActivate, Router } from '@angular/router';

@Injectable({ providedIn: 'root' })
export class AuthGuard implements CanActivate {
  constructor(private router: Router) {}

  canActivate(): boolean {
    const token = localStorage.getItem('token');
    if (!token) {
      this.router.navigate(['/login']);
      return false;
    }
    return true;
  }
}

// In routes:
// { path: 'admin', component: AdminComponent, canActivate: [AuthGuard] }
```

---

## RxJS Basics
*Reactive observables for async data*

**Observable** – Stream of values over time  
**subscribe()** – Start listening to an observable  
**pipe()** – Chain operators  

```typescript
import { map, catchError, tap } from 'rxjs/operators';
import { of } from 'rxjs';

this.usersService.getAll().pipe(
  tap(users => console.log('loaded', users.length)),
  map(users => users.filter(u => u.active)),
  catchError(err => {
    console.error(err);
    return of([]);    // fallback to empty array
  })
).subscribe(users => this.users = users);
```
