import { Component, OnInit } from '@angular/core';
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
export class SearchComponent implements OnInit {
  precision: any;
  recobrado: any;
  medidaF: any;
  medidaF1: any; 
  basicOptions: any;

  ngOnInit() {
      const documentStyle = getComputedStyle(document.documentElement);
      const textColor = documentStyle.getPropertyValue('--text-color');
      const textColorSecondary = documentStyle.getPropertyValue('--text-color-secondary');
      const surfaceBorder = documentStyle.getPropertyValue('--surface-border')  
      this.precision = {
          labels: ['Booleano', 'Booleano Extendido'],
          datasets: [
              {
                label: 'Sales',
                data: [0.540, 0.325],
                backgroundColor: ['rgba(255, 159, 64, 0.2)', 'rgba(75, 192, 192, 0.2)', 'rgba(54, 162, 235, 0.2)', 'rgba(153, 102, 255, 0.2)'],
                borderColor: ['rgb(255, 159, 64)', 'rgb(75, 192, 192)', 'rgb(54, 162, 235)', 'rgb(153, 102, 255)'],
                borderWidth: 1
              }
          ]
      } 

      this.recobrado = {
        labels: ['Booleano', 'Booleano Extendido'],
        datasets: [
            {
                label: 'Sales',
                data: [540, 325],
                backgroundColor: ['rgba(54, 162, 235, 0.2)', 'rgba(153, 102, 255, 0.2)'],
                borderColor: ['rgb(54, 162, 235)', 'rgb(153, 102, 255)'],
                borderWidth: 1
            }
        ]
    }

    this.medidaF = {
      labels: ['Booleano', 'Booleano Extendido'],
      datasets: [
          {
              label: 'Sales',
              data: [540, 325],
              backgroundColor: ['rgba(54, 162, 235, 0.2)', 'rgba(153, 102, 255, 0.2)'],
              borderColor: ['rgb(54, 162, 235)', 'rgb(153, 102, 255)'],
              borderWidth: 1
          }
      ]
    }

    this.medidaF1 = {
      labels: ['Booleano', 'Booleano Extendido'],
      datasets: [
          {
              label: 'Sales',
              data: [540, 325],
              backgroundColor: ['rgba(255, 159, 64, 0.2)', 'rgba(75, 192, 192, 0.2)'],
              borderColor: ['rgb(255, 159, 64)', 'rgb(75, 192, 192)'],
              borderWidth: 1
          }
      ]
    }

      this.basicOptions = {
          plugins: {
              legend: {
                  labels: {
                      color: textColor
                  }
              }
          },
          scales: {
              y: {
                  beginAtZero: true,
                  ticks: {
                      color: textColorSecondary
                  },
                  grid: {
                      color: surfaceBorder,
                      drawBorder: false
                  }
              },
              x: {
                  ticks: {
                      color: textColorSecondary
                  },
                  grid: {
                      color: surfaceBorder,
                      drawBorder: false
                  }
              }
          }
      };
  }
}
