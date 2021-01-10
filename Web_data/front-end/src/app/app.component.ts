import { Component } from '@angular/core';
import { BackendService } from './backend.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'front-end';
  armInverseStatus = 'Off';
  i = 0;
  lenOfCommands = 0;
  isProgrammingMode = false;
  isArmOn = true;
  isRewritingProgram = false;
  isSpadeToggled = false;
  programButtonText = 'New';

  commands: Map<number, string> = new Map();
  
  

  constructor(private service: BackendService) {
   }

  jsonify(map){
    if ( this.isArmOn ){
      let jsonObject = {};  
      let listtt = [];
      if (map.length > 1){
          listtt.push(map);
      } else {
          map.forEach((value) => {  
            listtt.push(value);
          });  
        }
        return JSON.stringify(listtt);
      }
    }
  sendJsonDoc(){
    if ( this.isArmOn ){
      return this.service.postCommands(this.jsonify(this.commands));
    }
  }

  switchOnOff(){
    if( this.isArmOn ) {

      this.isArmOn = false;
      this.armInverseStatus = "On";

    } else {

      this.isArmOn = true;
      this.armInverseStatus = "Off";

    }
  }

  spade(){
    let temp = '';
    if( this.isArmOn ){
      if( this.isSpadeToggled ) {

        this.isSpadeToggled = false;
        temp = 'Toggle Spade Off';
  
      } else {
  
        this.isSpadeToggled = true;
        temp = 'Toggle Spade On';
  
      }
    }
    if( this.isProgrammingMode == false ){

      this.postCommands(this.jsonify(temp));
      
    } else if( this.isProgrammingMode == true && this.isRewritingProgram == true){

      this.i++;
      this.commands.set(this.i, temp);

    }
    
  }

  resetAll(){
    return this.service.resetAll();
  }

  getLenght(data){
    length = 0;
    for (var count in data.keys) {
      length++;
    }
    this.lenOfCommands = length;
  }

  manual(){
    this.isProgrammingMode == false;
    this.isRewritingProgram == false;
  }

  newItem(data: string){
    if( this.isProgrammingMode == false && this.isRewritingProgram == false ){

      this.postCommands(this.jsonify(data));
      
    } else if( this.isProgrammingMode == true && this.isRewritingProgram == true){

      this.i++;
      this.commands.set(this.i, data);

    }
    
  }
  removeItem(index){
    if(this.isProgrammingMode == true){
      this.commands.delete(index);
    }
  }
  postCommands(commands: any) {
    this.service.postCommands(commands);
  }
  switchModeProgramming(){
    if( this.isProgrammingMode ) {

      this.isProgrammingMode = false;

    } else {

      this.isProgrammingMode = true;

    }
  }
  programEditor() {
    if( this.isProgrammingMode == true ){

      if( this.isRewritingProgram == true ){

        this.isRewritingProgram = false;
        this.programButtonText = 'Delete';

      } else if( this.isRewritingProgram == false ){

        this.service.resetAll();
        this.commands.clear();
        this.i = 0;
        this.isRewritingProgram = true;
        this.programButtonText = 'Save';

      }
    }
  }
}
