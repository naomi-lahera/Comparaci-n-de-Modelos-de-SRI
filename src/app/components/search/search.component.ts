import { Component } from '@angular/core';
import { PrimeNgModule } from '../../prime-ng/prime-ng.module';
import { MenuItem } from 'primeng/api';
import { RouterModule } from '@angular/router';

@Component({
  selector: 'app-search',
  standalone: true,
  imports: [
    PrimeNgModule,
    RouterModule
  ],
  templateUrl: './search.component.html',
  styleUrl: './search.component.css'
})
export class SearchComponent {
  query!: string;
  model!: string;
}
