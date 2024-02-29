import { Component } from '@angular/core';
import { PrimeNgModule } from '../../prime-ng/prime-ng.module';
import { RouterModule } from '@angular/router';

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [
    PrimeNgModule,
    RouterModule
  ],
  templateUrl: './home.component.html',
  styleUrl: './home.component.css'
})
export class HomeComponent {

}
