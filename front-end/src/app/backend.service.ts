import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';


@Injectable()
export class BackendService {

  constructor(private http: HttpClient) { }
  backendUrl = "http://localhost:5000/com";

  postCommands(commamnds) {
    var formData: any = new FormData();
    formData.append("data", commamnds);
    return  this.http.post(this.backendUrl, formData).subscribe(
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
