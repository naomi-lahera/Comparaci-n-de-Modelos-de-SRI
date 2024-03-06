import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DocsDialogComponent } from './docs-dialog.component';

describe('ReturnedDocsComponent', () => {
  let component: DocsDialogComponent;
  let fixture: ComponentFixture<DocsDialogComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [DocsDialogComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(DocsDialogComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
