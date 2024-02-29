import { NgModule } from '@angular/core';
import { CheckboxModule } from 'primeng/checkbox';
import { CommonModule } from '@angular/common';
import { ButtonModule } from 'primeng/button';
import { FormsModule } from '@angular/forms';
import { InputGroupModule } from 'primeng/inputgroup';
import { InputGroupAddonModule } from 'primeng/inputgroupaddon';
import { InputTextModule } from 'primeng/inputtext';
import { MenubarModule } from 'primeng/menubar';
import { MenuModule } from 'primeng/menu';
import { RadioButtonModule } from 'primeng/radiobutton';
import { RippleModule } from 'primeng/ripple';

@NgModule({
  declarations: [],
  imports: [
    CommonModule
  ],
  exports:[
    CheckboxModule,
    CommonModule,
    ButtonModule,
    FormsModule,
    InputGroupModule,
    InputGroupAddonModule,
    InputTextModule,
    MenubarModule,
    MenuModule,
    RadioButtonModule,  
    RippleModule
  ]
})
export class PrimeNgModule { }
