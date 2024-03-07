import { Component, OnInit } from '@angular/core';
import { PrimeNgModule } from '../../prime-ng/prime-ng.module';
import { RouterModule } from '@angular/router';
import { MetricsService } from '../../services/metrics.service';
import { MetricResult } from '../../interfaces/metric-result';

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
export class HomeComponent implements OnInit {
  data: any;

  options: any;

  precision!: MetricResult;
  constructor(private metricService: MetricsService) {}

    async ngOnInit() {
        this.precision = await this.metricService.getMetric('Precision')
        
        console.log('precision: ')
        console.log(this.precision)

        const documentStyle = getComputedStyle(document.documentElement);
        const textColor = documentStyle.getPropertyValue('--text-color');
        const textColorSecondary = documentStyle.getPropertyValue('--text-color-secondary');
        const surfaceBorder = documentStyle.getPropertyValue('--surface-border')       
        this.data = {
            labels: this.precision.queries_id,
            datasets: [
                {
                    label: 'Boolean',
                    data: this.precision.boolean,
                    fill: false,
                    borderColor: documentStyle.getPropertyValue('--blue-500'),
                    tension: 0.4
                },
                {
                    label: 'Extended Boolean',
                    data: this.precision.extended,
                    fill: false,
                    borderColor: documentStyle.getPropertyValue('--pink-500'),
                    tension: 0.4
                }
            ]
        }      
        this.options = {
            maintainAspectRatio: false,
            aspectRatio: 0.6,
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
                        color: textColorSecondary
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
