import { Component, OnInit } from '@angular/core';
import { Category } from 'src/app/models/category.model';
import { CategoryService } from 'src/app/services/category.service';
import { ActivatedRoute, Router } from '@angular/router';

@Component({
  selector: 'app-category-details',
  templateUrl: './category-details.component.html',
  styleUrls: ['./category-details.component.css']
})
export class CategoryDetailsComponent implements OnInit {

  currentCategory: Category;
  message = '';

  constructor(
    private categoryService: CategoryService,
    private route: ActivatedRoute,
    private router: Router) { 
      
    }

  ngOnInit(): void {
    this.message = '';
    this.getCategory(this.route.snapshot.params.id);
    
  }

  getCategory(id: string): void {
    this.categoryService.get(id)
      .subscribe(
        data => {
          this.currentCategory = data;
        },
        error => {
          console.log(error);
        });
  }


  updateCategory(): void {
    this.categoryService.update(this.currentCategory.categoryID, this.currentCategory)
      .subscribe(
        response => {
          console.log(response);
          this.message = response.message;
        },
        error => {
          console.log(error);
        });
  }

  deleteCategory(): void {
    this.categoryService.delete(this.currentCategory.categoryID)
      .subscribe(
        response => {
          console.log(response);
          this.router.navigate(['/categories']);
        },
        error => {
          console.log(error);
        });
  }
  
}
