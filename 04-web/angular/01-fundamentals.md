# Angular Fundamentals
*TypeScript-based frontend framework by Google*

## What is Angular
*Full framework for single-page apps*

**Angular** – Opinionated TypeScript framework for building SPAs  
**SPA (Single-Page App)** – Browser loads one HTML page; navigation handled by JS  
**Module** – Container grouping related components, services, pipes  
**Component** – UI building block: template + logic + styles  
**Service** – Shared business logic / data access layer  
**Directive** – Instruction to modify DOM elements  
**Pipe** – Transform data for display  

---

## Setup
*Install CLI and create project*

```bash
npm install -g @angular/cli
ng new my-app --routing --style=scss
cd my-app
ng serve           # http://localhost:4200

ng generate component users       # ng g c users
ng generate service users         # ng g s users
ng generate module users          # ng g m users
ng build --prod                   # production build
```

---

## Component
*Template + class + decorator*

```typescript
// users.component.ts
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-users',        // use as <app-users>
  templateUrl: './users.component.html',
  styleUrls: ['./users.component.scss']
})
export class UsersComponent implements OnInit {
  title = 'Users List';
  users: string[] = [];

  ngOnInit(): void {
    this.users = ['Alice', 'Bob'];
  }
}
```

```html
<!-- users.component.html -->
<h1>{{ title }}</h1>
<ul>
  <li *ngFor="let user of users">{{ user }}</li>
</ul>
```

---

## Data Binding
*Sync data between component and template*

**Interpolation** – `{{ value }}` – display component property  
**Property binding** – `[src]="imageUrl"` – set DOM property  
**Event binding** – `(click)="onClick()"` – listen to DOM event  
**Two-way binding** – `[(ngModel)]="name"` – read + write  

```html
<img [src]="user.avatar">
<button (click)="deleteUser(user.id)">Delete</button>
<input [(ngModel)]="searchTerm">
<p>Searching: {{ searchTerm }}</p>
```

---

## Built-in Directives
*Structural and attribute directives*

```html
<!-- Structural: modify DOM structure -->
<div *ngIf="isLoggedIn">Welcome back!</div>
<li *ngFor="let item of items; let i = index">{{ i }}: {{ item }}</li>
<div [ngSwitch]="role">
  <p *ngSwitchCase="'admin'">Admin panel</p>
  <p *ngSwitchDefault>User panel</p>
</div>

<!-- Attribute: modify element appearance -->
<div [ngClass]="{ active: isActive, disabled: !isEnabled }"></div>
<div [ngStyle]="{ color: textColor, fontSize: '14px' }"></div>
```

---

## Pipes
*Transform template values*

```html
{{ price | currency:'USD' }}        <!-- $1,500.00 -->
{{ date | date:'yyyy-MM-dd' }}      <!-- 2024-01-15 -->
{{ name | uppercase }}              <!-- ALICE -->
{{ text | slice:0:50 }}             <!-- truncate -->
{{ data | json }}                   <!-- debug objects -->
{{ number | number:'1.2-2' }}       <!-- 1,500.00 -->
```
