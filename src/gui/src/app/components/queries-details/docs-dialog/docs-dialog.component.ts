import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
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
    DialogService
  ],
  templateUrl: './docs-dialog.component.html',
  styleUrl: './docs-dialog.component.css'
})
export class DocsDialogComponent {

  constructor(public ref: DynamicDialogRef, public configuration: DynamicDialogConfig) {}

  docs: Doc[] = [
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
    },
    {
      title: 'Documnent title',
      text: 'Document text'
    }
  ]

  deleteProduct(doc: Doc) {
  }

  onCancel() {
    if (this.ref) {
        this.ref.close();
    }
  }
}
