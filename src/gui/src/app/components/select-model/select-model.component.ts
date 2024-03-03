import { Component } from '@angular/core';
import { PrimeNgModule } from '../../prime-ng/prime-ng.module';
import { RouterModule } from '@angular/router';
import { Model } from '../../interfaces/model';

@Component({
  selector: 'app-select-model',
  standalone: true,
  imports: [
    PrimeNgModule,
    RouterModule
  ],
  templateUrl: './select-model.component.html',
  styleUrl: './select-model.component.css'
})
export class SelectModelComponent {
  models: Model[] = [
    {
      name: 'Booleano Difuso',
      description: [
        'Es una extensión del modelo booleano tradicional.',
        'Asigna un grado de pertenencia a cada término en un documento. ',
        'Al permitir grados de pertenencia, el modelo booleano difuso puede proporcionar resultados de búsqueda más relevantes.'
      ]
    },
    {
      name: 'Booleano Extendido',
      description: [
        'Es una extensión del modelo booleano tradicional.',
        'Al igual que en el modelo vectorial, en el Modelo Booleano Extendido, un documento se representa por un vector.',
        'Permite operaciones lógicas como AND, OR y NOT, que se utilizan para combinar términos en una consulta.'
      ]
    },
    {
      name: 'Semántica Latente',
      description: [
        'Genera conceptos abstractos o latentes que representan temas o significados subyacentes en los textos.',
        'Reduce la dimensionalidad del espacio semántico al capturar las relaciones entre palabras y documentos a través de conceptos latentes.',
        'Abordar el problema de la polisemia y sinónimos.'
      ]
    }
  ];
}
