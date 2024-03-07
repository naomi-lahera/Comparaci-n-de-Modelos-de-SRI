import { Component, OnInit } from '@angular/core';
import { PrimeNgModule } from '../../prime-ng/prime-ng.module';
import { MenuItem } from 'primeng/api';
import { RouterModule } from '@angular/router';
import { MetricResult } from '../../interfaces/metric-result';
import { MetricsService } from '../../services/metrics.service';

@Component({
  selector: 'app-data',
  standalone: true,
  imports: [
    PrimeNgModule,
    RouterModule
  ],
  templateUrl: './data.component.html',
  styleUrl: './data.component.css'
})
export class DataComponent implements OnInit {
  recobrado: any;
  recobradoData!: MetricResult;
  medidaF: any;
  medidaFData!: MetricResult;
  medidaF1: any; 
  medidaF1Data!: MetricResult;
  exactitud: any;
  exactitudData!: MetricResult;
  options: any;
  data: any;

  constructor(private metricservice: MetricsService) {}

  async ngOnInit() {
      this.recobradoData = await this.metricservice.getMetric('Recall');
      console.log(this.recobrado)
      this.medidaFData = await this.metricservice.getMetric('F-measure');
      this.medidaF1Data = await this.metricservice.getMetric('F1-measure');
      this.exactitudData = await this.metricservice.getMetric('Accuracy');
      const documentStyle = getComputedStyle(document.documentElement);
      const textColor = documentStyle.getPropertyValue('--text-color');
      const textColorSecondary = documentStyle.getPropertyValue('--text-color-secondary');
      const surfaceBorder = documentStyle.getPropertyValue('--surface-border')  
      this.exactitud = {
          labels: this.exactitudData.queries_id,
          datasets: [
              {
                label: 'Boolean',
                data: this.exactitudData.boolean,
                fill: false,
                // backgroundColor: ['rgba(255, 159, 64, 0.2)', 'rgba(75, 192, 192, 0.2)', 'rgba(54, 162, 235, 0.2)', 'rgba(153, 102, 255, 0.2)'],
                borderColor: 'rgb(54, 162, 235)',
                // borderWidth: 1
                tension: 0.4
              },
              {
                label: 'Extended Boolean',
                data: this.exactitudData.extended,
                fill: false,
                // backgroundColor: ['rgba(255, 159, 64, 0.2)', 'rgba(75, 192, 192, 0.2)', 'rgba(54, 162, 235, 0.2)', 'rgba(153, 102, 255, 0.2)'],
                borderColor: 'rgb(153, 102, 255)',
                // borderWidth: 1
                tension: 0.4
              }
          ]
      } 

      this.recobrado = {
        labels: this.recobradoData.queries_id,
        datasets: [
            {
                label: 'Boolean',
                data: this.recobradoData.boolean,
                fill: false,
                // backgroundColor: ['rgba(54, 162, 235, 0.2)', 'rgba(153, 102, 255, 0.2)'],
                borderColor: 'rgb(153, 102, 255)',
                // borderWidth: 1
                tension: 0.4
            },
            {
                label: 'Extended Boolean',
                data: this.recobradoData.extended,
                fill: false,
                // backgroundColor: ['rgba(54, 162, 235, 0.2)', 'rgba(153, 102, 255, 0.2)'],
                borderColor: documentStyle.getPropertyValue('--pink-500'),
                // borderWidth: 1
                tension: 0.4
            }

        ]
    }

    this.medidaF = {
        labels: this.medidaFData.queries_id,
        datasets: [
            {
                label: 'Boolean',
                data: this.medidaFData.boolean,
                fill: false,
                // backgroundColor: ['rgba(54, 162, 235, 0.2)', 'rgba(153, 102, 255, 0.2)'],
                borderColor: 'rgb(153, 102, 255)',
                // borderWidth: 1
                tension: 0.4
            },
            {
                label: 'Extended Boolean',
                data: this.medidaFData.extended,
                fill: false,
                // backgroundColor: ['rgba(54, 162, 235, 0.2)', 'rgba(153, 102, 255, 0.2)'],
                borderColor: documentStyle.getPropertyValue('--pink-500'),
                // borderWidth: 1
                tension: 0.4
            }

        ]
    }

    this.medidaF1 = {
        labels: this.medidaF1Data.queries_id,
        datasets: [
            {
              label: 'Boolean',
              data: this.medidaF1Data.boolean,
              fill: false,
              // backgroundColor: ['rgba(255, 159, 64, 0.2)', 'rgba(75, 192, 192, 0.2)', 'rgba(54, 162, 235, 0.2)', 'rgba(153, 102, 255, 0.2)'],
              borderColor: 'rgb(54, 162, 235)',
              // borderWidth: 1
              tension: 0.4
            },
            {
              label: 'Extended Boolean',
              data: this.medidaF1Data.extended,
              fill: false,
              // backgroundColor: ['rgba(255, 159, 64, 0.2)', 'rgba(75, 192, 192, 0.2)', 'rgba(54, 162, 235, 0.2)', 'rgba(153, 102, 255, 0.2)'],
              borderColor: 'rgb(153, 102, 255)',
              // borderWidth: 1
              tension: 0.4
            }
        ]
    }

    this.options = {
        maintainAspectRatio: false,
        aspectRatio: 0.8,
        plugins: {
            legend: {
                labels: {
                    color: textColor
                }
            }
        },
        scales: {
            x: {
                ticks: {
                    color: textColorSecondary,
                    font: {
                        weight: 500
                    }
                },
                grid: {
                    color: surfaceBorder,
                    drawBorder: false
                }
            },
            y: {
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
