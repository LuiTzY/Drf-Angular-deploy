import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { HelloResponse } from '../interfaces/hello';


@Injectable({
  providedIn: 'root'
})
export class HelloService {

  private localUrl: string =  'http://localhost:8000/';
  private publicUrl: string = 'https://backend/'; 
  constructor(private httpClient: HttpClient) { }

  getHello() {
    return this.httpClient.get<HelloResponse>(this.publicUrl+'hello/');
  }
}
