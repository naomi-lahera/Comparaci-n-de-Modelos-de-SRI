import { Routes } from '@angular/router';
import { HomeComponent } from './components/home/home.component';
import { DataComponent } from './components/data/data.component';
import { SelectModelComponent } from './components/select-model/select-model.component';
import { QueriesDetailsComponent } from './components/queries-details/queries-details.component';

export const routes: Routes = [
    {path: '', component: HomeComponent},
    {path: 'search', component: QueriesDetailsComponent},
    // {path: 'select-model', component: SelectModelComponent},
    {path: 'data', component: DataComponent}
];
