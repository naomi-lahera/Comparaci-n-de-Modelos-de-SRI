import { CommonModule } from '@angular/common';
import { Component, OnInit} from '@angular/core';
import { ConfirmationService } from 'primeng/api';
import { DialogService, DynamicDialogConfig, DynamicDialogRef } from "primeng/dynamicdialog";
import { PrimeNgModule } from '../../../prime-ng/prime-ng.module';
import { Doc } from '../../../interfaces/doc';
import { QueriesService } from '../../../services/queries.service';
import { Query } from '../../../interfaces/query';
import { HttpClientModule } from '@angular/common/http';


@Component({
  selector: 'app-returned-docs',
  standalone: true,
  imports: [
    CommonModule,
    PrimeNgModule,
    HttpClientModule
  ],
  providers: [
    DialogService,
    ConfirmationService,
  ],
  templateUrl: './docs-dialog.component.html',
  styleUrl: './docs-dialog.component.css'
})
export class DocsDialogComponent implements OnInit {
  constructor(private qService: QueriesService, public ref: DynamicDialogRef, public configuration: DynamicDialogConfig, private confirmationService: ConfirmationService) {}
  
  async ngOnInit() {
    this.query = this.configuration.data as Query;
    this.docs = await this.qService.getDocs(this.query.id)
  }

  query!: Query;
  docs!: Doc[];
  // [
  //   {
  //     id: 'tcfvyhjm',
  //     title: 'Documnent title sxtdcrfgyioijo´pl´poiuytrteedf67i oijlktdu6fyknkuljjni yuecdvi77iuolklictxrezatsxeyrt7yu9i0opoui 097reder5g679p8jpiomkjhg56879ouijk',
  //     text: 'Document text'
  //   },
  //   {
  //     id: 'tcfvyhjm',
  //     title: 'Documnent title sxtdcrfgyioijo´pl´poiuytrteedf67i oijlktdu6fyknkuljjni yuecdvi77iuolklictxrezatsxeyrt7yu9i0opoui 097reder5g679p8jpiomkjhg56879ouijk',
  //     text: 'Document text'
  //   },
  //   {
  //     id: 'tcfvyhjm',
  //     title: 'Documnent title sxtdcrfgyioijo´pl´poiuytrteedf67i oijlktdu6fyknkuljjni yuecdvi77iuolklictxrezatsxeyrt7yu9i0opoui 097reder5g679p8jpiomkjhg56879ouijk',
  //     text: 'Document text'
  //   },
  //   {
  //     id: 'tcfvyhjm',
  //     title: 'Documnent title sxtdcrfgyioijo´pl´poiuytrteedf67i oijlktdu6fyknkuljjni yuecdvi77iuolklictxrezatsxeyrt7yu9i0opoui 097reder5g679p8jpiomkjhg56879ouijk',
  //     text: 'Document text'
  //   },
  //   {
  //     id: 'tcfvyhjm',
  //     title: 'Documnent title sxtdcrfgyioijo´pl´poiuytrteedf67i oijlktdu6fyknkuljjni yuecdvi77iuolklictxrezatsxeyrt7yu9i0opoui 097reder5g679p8jpiomkjhg56879ouijk',
  //     text: 'Document text'
  //   },
  //   {
  //     id: 'tcfvyhjm',
  //     title: 'Documnent title sxtdcrfgyioijo´pl´poiuytrteedf67i oijlktdu6fyknkuljjni yuecdvi77iuolklictxrezatsxeyrt7yu9i0opoui 097reder5g679p8jpiomkjhg56879ouijk',
  //     text: 'Document text'
  //   },
  //   {
  //     id: 'tcfvyhjm',
  //     title: 'Documnent title sxtdcrfgyioijo´pl´poiuytrteedf67i oijlktdu6fyknkuljjni yuecdvi77iuolklictxrezatsxeyrt7yu9i0opoui 097reder5g679p8jpiomkjhg56879ouijk',
  //     text: 'Document text'
  //   },
  //   {
  //     id: 'tcfvyhjm',
  //     title: 'Documnent title sxtdcrfgyioijo´pl´poiuytrteedf67i oijlktdu6fyknkuljjni yuecdvi77iuolklictxrezatsxeyrt7yu9i0opoui 097reder5g679p8jpiomkjhg56879ouijk',
  //     text: 'Document text'
  //   },
  //   {
  //     id: 'tcfvyhjm',
  //     title: 'Documnent title sxtdcrfgyioijo´pl´poiuytrteedf67i oijlktdu6fyknkuljjni yuecdvi77iuolklictxrezatsxeyrt7yu9i0opoui 097reder5g679p8jpiomkjhg56879ouijk',
  //     text: 'Document text'
  //   },
  //   {
  //     id: 'tcfvyhjm',
  //     title: 'Documnent title sxtdcrfgyioijo´pl´poiuytrteedf67i oijlktdu6fyknkuljjni yuecdvi77iuolklictxrezatsxeyrt7yu9i0opoui 097reder5g679p8jpiomkjhg56879ouijk',
  //     text: 'Document text'
  //   },
  //   {
  //     id: 'tcfvyhjm',
  //     title: 'Documnent title sxtdcrfgyioijo´pl´poiuytrteedf67i oijlktdu6fyknkuljjni yuecdvi77iuolklictxrezatsxeyrt7yu9i0opoui 097reder5g679p8jpiomkjhg56879ouijk',
  //     text: 'Document text'
  //   },
  //   {
  //     id: 'tcfvyhjm',
  //     title: 'Documnent title sxtdcrfgyioijo´pl´poiuytrteedf67i oijlktdu6fyknkuljjni yuecdvi77iuolklictxrezatsxeyrt7yu9i0opoui 097reder5g679p8jpiomkjhg56879ouijk',
  //     text: 'Document text'
  //   },
  //   {
  //     id: 'tcfvyhjm',
  //     title: 'Documnent title sxtdcrfgyioijo´pl´poiuytrteedf67i oijlktdu6fyknkuljjni yuecdvi77iuolklictxrezatsxeyrt7yu9i0opoui 097reder5g679p8jpiomkjhg56879ouijk',
  //     text: 'Document text'
  //   },
  //   {
  //     id: 'tcfvyhjm',
  //     title: 'Documnent title sxtdcrfgyioijo´pl´poiuytrteedf67i oijlktdu6fyknkuljjni yuecdvi77iuolklictxrezatsxeyrt7yu9i0opoui 097reder5g679p8jpiomkjhg56879ouijk',
  //     text: 'Document text'
  //   }
  // ]

  deleteDoc(doc: Doc){
    console.log('doc');
  }

  async confirm1(event: Event, doc: Doc) {
    this.confirmationService.confirm({
        target: event.target as EventTarget,
        message: 'Quiere eliminar la relacion de este documento con esta query?',
        icon: 'pi pi-exclamation-triangle',
        accept: async () => {
            await this.qService.deleteDoc(this.query.id, doc.id)
            this.ngOnInit()
            // this.docs = await this.qService.getDocs(this.query.id)  
            console.log('update done')      
          }
    });
  }

  onCancel() {
    if (this.ref) {
        this.ref.close();
    }
  }
}
