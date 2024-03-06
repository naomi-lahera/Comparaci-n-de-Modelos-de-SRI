import { ComponentFixture, TestBed } from '@angular/core/testing';

import { QueriesDetailsComponent } from './queries-details.component';

describe('QueriesDetailsComponent', () => {
  let component: QueriesDetailsComponent;
  let fixture: ComponentFixture<QueriesDetailsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [QueriesDetailsComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(QueriesDetailsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
