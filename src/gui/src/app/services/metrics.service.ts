import { HttpClient, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { MetricResult } from '../interfaces/metric-result';
import { firstValueFrom, retry } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class MetricsService {
  private apiUrl = 'http://localhost:4000';
  constructor(private httpClient: HttpClient) { }

  async getMetric(metric: string): Promise<MetricResult>{
    let params = new HttpParams().set('metric', metric);
    return await firstValueFrom(this.httpClient.get<MetricResult>(`${this.apiUrl}/api/get-metric`, {params: params}))
      .then(response => {
        console.log('Get Metric Done')
        return response as MetricResult
      })
  }
}
