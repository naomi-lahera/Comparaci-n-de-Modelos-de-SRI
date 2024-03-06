import { Component} from '@angular/core';
import { PrimeNgModule } from '../../prime-ng/prime-ng.module';
import { CommonModule } from '@angular/common';
import { DocsDialogComponent } from './docs-dialog/docs-dialog.component';
import { Query } from '../../interfaces/query';
import { DialogService, DynamicDialogRef } from 'primeng/dynamicdialog';
import { MessageService } from 'primeng/api';
import { RouterModule } from '@angular/router';

@Component({
  selector: 'app-queries-details',
  standalone: true,
  imports: [
    CommonModule,
    PrimeNgModule,
    RouterModule,
  ],
  providers: [
    DialogService,
    MessageService
  ],
  templateUrl: './queries-details.component.html',
  styleUrl: './queries-details.component.css'
})
export class QueriesDetailsComponent {

  constructor(private dialogService: DialogService, private messageService: MessageService) { }

  ref: DynamicDialogRef | undefined;
  queires: Query[] = [
    {
      text: 'text_0',
      id: '0'
    },
    {
      text: 'text_0',
      id: '0'
    },
    {
      text: 'text_0',
      id: '0'
    },
    {
      text: 'text_0',
      id: '0'
    },
    {
      text: 'text_0',
      id: '0'
    },
    {
      text: 'text_0',
      id: '0'
    },
    {
      text: 'text_0',
      id: '0'
    },
    {
      text: 'text_0',
      id: '0'
    },
    {
      text: 'text_0',
      id: '0'
    }
  ]

  async showDocsDialog(query: Query) {
    this.ref = this.dialogService.open(DocsDialogComponent, {
        header: 'Returned Docs',
        styleClass: 'w-full md:w-9 h-full',
        contentStyle: { overflow: 'auto' },
        maximizable: true,
        modal: true,
        data: query
    });
  }

  ngOnDestroy(): void {
    if (this.ref) {
      this.ref.close();
    }
  }

}
