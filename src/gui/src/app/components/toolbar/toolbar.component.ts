import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { PrimeNgModule } from '../../prime-ng/prime-ng.module';
import { RouterModule } from '@angular/router';
import { MenuItem } from 'primeng/api';

@Component({
  selector: 'app-toolbar',
  standalone: true,
  imports: [
    CommonModule,
    PrimeNgModule,
    RouterModule
  ],
  templateUrl: './toolbar.component.html',
  styleUrl: './toolbar.component.css'
})
export class ToolbarComponent {
  sidebarVisible: boolean = false;
  items: MenuItem[] | undefined;

  ngOnInit() {
    this.items = [
        {
            label: 'File',
            icon: 'pi pi-file',
            items: [
                {
                    label: 'New',
                    icon: 'pi pi-plus',
                    items: [
                              {
                                  label: 'Document',
                                  icon: 'pi pi-file'
                              },
                              {
                                  label: 'Image',
                                  icon: 'pi pi-image'
                              },
                              {
                                  label: 'Video',
                                  icon: 'pi pi-video'
                              }
                          ]
                      },
                      {
                          label: 'Open',
                          icon: 'pi pi-folder-open'
                      },
                      {
                          label: '# print',
                          icon: 'pi pi-# print'
                      }
                  ]
              },
              {
                  label: 'Edit',
                  icon: 'pi pi-file-edit',
                  items: [
                      {
                          label: 'Copy',
                          icon: 'pi pi-copy'
                      },
                      {
                          label: 'Delete',
                          icon: 'pi pi-times'
                      }
                  ]
              },
              {
                  label: 'Search',
                  icon: 'pi pi-search'
              },
              {
                  separator: true
              },
              {
                  label: 'Share',
                  icon: 'pi pi-share-alt',
                  items: [
                      {
                          label: 'Slack',
                          icon: 'pi pi-slack'
                      },
                      {
                          label: 'Whatsapp',
                          icon: 'pi pi-whatsapp'
                      }
                  ]
              }
          ]
      }
}
