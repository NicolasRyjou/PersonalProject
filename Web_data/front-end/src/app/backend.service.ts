import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';


@Injectable()
export class BackendService {

  constructor(private http: HttpClient) { }
  backendUrl = "http://nicolasryjou.pythonanywhere.com/api";

  postCommands(commands) {
    return  this.http.post(this.backendUrl, commands).subscribe(
      (response) => console.log(response),
      (error) => console.log(error)
    );
  }

  getCommands() {
    return  this.http.get(this.backendUrl).subscribe(
      (response) => console.log(response),
      (error) => console.log(error)
    );
  }
  resetAll(){
    return  this.http.delete(this.backendUrl);
  }
}
