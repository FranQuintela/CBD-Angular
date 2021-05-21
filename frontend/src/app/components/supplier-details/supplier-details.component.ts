import { Component, OnInit } from '@angular/core';
import { Supplier } from 'src/app/models/supplier.model';
import { SupplierService } from 'src/app/services/supplier.service';
import { ActivatedRoute, Router } from '@angular/router';

@Component({
  selector: 'app-supplier-details',
  templateUrl: './supplier-details.component.html',
  styleUrls: ['./supplier-details.component.css']
})
export class SupplierDetailsComponent implements OnInit {

  currentSupplier: Supplier;
  message = '';

  constructor(
    private supplierService: SupplierService,
    private route: ActivatedRoute,
    private router: Router) { 
      
    }

  ngOnInit(): void {
    this.message = '';
    this.getSupplier(this.route.snapshot.params.id);
    
  }

  getSupplier(id: string): void {
    this.supplierService.get(id)
      .subscribe(
        data => {
          this.currentSupplier = data;
        },
        error => {
          console.log(error);
        });
  }


  updateSupplier(): void {
    this.supplierService.update(this.currentSupplier.supplierID, this.currentSupplier)
      .subscribe(
        response => {
          console.log(response);
          this.message = response.message;
        },
        error => {
          console.log(error);
        });
  }

  deleteSupplier(): void {
    this.supplierService.delete(this.currentSupplier.supplierID)
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
