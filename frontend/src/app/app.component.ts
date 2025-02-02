import { Component, OnInit } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { HelloService } from './services/hello.service';
import { HelloResponse } from './interfaces/hello';

@Component({
  selector: 'app-root',
  imports: [RouterOutlet],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent implements OnInit{
  title = 'frontend';
  public response!:HelloResponse;
  constructor(private helloService: HelloService){}

  getHello(){
    this.helloService.getHello().subscribe({
      next: (response) => { 
        console.log(response)
        this.response =  response;
      },
      error: (err)=>{console.log(err)}
    })
  }

  ngOnInit(): void {
    this.getHello();
  }
}
