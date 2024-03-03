import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SelectModelComponent } from './select-model.component';

describe('SelectModelComponent', () => {
  let component: SelectModelComponent;
  let fixture: ComponentFixture<SelectModelComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [SelectModelComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(SelectModelComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
