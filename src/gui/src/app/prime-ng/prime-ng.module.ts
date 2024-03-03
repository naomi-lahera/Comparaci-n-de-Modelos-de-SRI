import { ButtonModule } from 'primeng/button';
import { NgModule } from '@angular/core';
import { CheckboxModule } from 'primeng/checkbox';
import { ChartModule } from 'primeng/chart';
import { CommonModule } from '@angular/common';
import { DividerModule } from 'primeng/divider';
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
    ButtonModule,
    CheckboxModule,
    ChartModule,
    CommonModule,
    DividerModule,
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
