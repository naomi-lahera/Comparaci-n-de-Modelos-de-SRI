import { HttpClient, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Query } from '../interfaces/query';
import { firstValueFrom } from 'rxjs';
import { Doc } from '../interfaces/doc';

@Injectable({
  providedIn: 'root',
})
export class QueriesService {
  private apiUrl = 'http://localhost:4000';
  constructor(private httpClient: HttpClient) {}

  async getQueries(): Promise<Query[]>{
    return await firstValueFrom(this.httpClient.get<Query[]>(`${this.apiUrl}/api/get_queries`)).
      then(response => {
        console.log('get queries service');
        return response as Query[];
      })
  }

  async getDocs(query_id: string): Promise<Doc[]>{
    let params = new HttpParams().set('query_id', query_id)
    return await firstValueFrom(this.httpClient.get<Doc[]>(`${this.apiUrl}/api/search`, {params: params}))
      .then(response => {
        console.log('get documents service');
        return response as Doc[];
      })
  }

  async deleteDoc(query_id: string, doc_id: string) {
    let params = new HttpParams().set('query_id', query_id).set('doc_id', doc_id);
    return await this.httpClient.delete(`${this.apiUrl}/api/delete-doc`, {params: params})
  }
}
