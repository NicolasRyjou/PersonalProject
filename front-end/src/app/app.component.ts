import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'front-end';
  armInverseStatus = 'Off';
  clawsClosing = 'Off';
  i = 0;
  lenOfCommands = 0;
  commands = {
    1:"test_1",
    2:"test_2",
    3:"test_1",
    4:"test_1",
    5:"test_2",
    6:"test_1",
    7:"test_1",
    8:"test_2",
    9:"test_1",
    10:"test_2",
    11:"test_1",
    12:"test_2",
    13:"test_1"
  };
  selection = 't';

  getLenght(data){
    length = 0;
    for (var count in data.keys) {
      length++;
    }
    this.lenOfCommands = length;
  }

  addItem(data: string){
    this.i++;
    this.commands[this.i] = data;
  }
  removeItem(index){
    delete this.commands[index];
  }
}
