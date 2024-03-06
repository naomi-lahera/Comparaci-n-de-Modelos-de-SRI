import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { ConfirmationService, MessageService } from 'primeng/api';
import { DialogService, DynamicDialogConfig, DynamicDialogRef } from "primeng/dynamicdialog";
import { PrimeNgModule } from '../../../prime-ng/prime-ng.module';
import { Doc } from '../../../interfaces/doc';


@Component({
  selector: 'app-returned-docs',
  standalone: true,
  imports: [
    CommonModule,
    PrimeNgModule,
  ],
  providers: [
    DialogService,
    ConfirmationService,
    MessageService
  ],
  templateUrl: './docs-dialog.component.html',
  styleUrl: './docs-dialog.component.css'
})
export class DocsDialogComponent {
  constructor(public ref: DynamicDialogRef, public configuration: DynamicDialogConfig, private confirmationService: ConfirmationService, private messageService: MessageService) {}

  docs: Doc[] = [
    {
      title: 'Documnent title sxtdcrfgyioijo´pl´poiuytrteedf67i oijlktdu6fyknkuljjni yuecdvi77iuolklictxrezatsxeyrt7yu9i0opoui 097reder5g679p8jpiomkjhg56879ouijk',
      text: 'Document text'
    },
    {
      title: 'Documnent title',
      text: 'Document text'
    },
    {
      title: 'Documnent title',
      text: 'Document text'
    },
    {
      title: 'Documnent title',
      text: 'Document text'
    },
    {
      title: 'Documnent title',
      text: 'Document text'
    },
    {
      title: 'Documnent title',
      text: 'Document text'
    },
    {
      title: 'Documnent title',
      text: 'Document text'
    }
  ]

  deleteDoc(doc: Doc){
    console.log('doc');
  }

  confirm1(event: Event, doc: Doc) {
    this.confirmationService.confirm({
        target: event.target as EventTarget,
        message: 'Quiere eliminar la relacion de este documento con esta query?',
        icon: 'pi pi-exclamation-triangle',
        accept: () => {
            this.messageService.add({ severity: 'info', summary: 'Confirmed', detail: 'You have accepted', life: 3000 });
        }
    });
  }

  onCancel() {
    if (this.ref) {
        this.ref.close();
    }
  }
}
