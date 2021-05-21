import { Component, OnInit } from '@angular/core';
import { Supplier } from 'src/app/models/supplier.model';
import { SupplierService } from 'src/app/services/supplier.service';

@Component({
  selector: 'app-suppliers-list',
  templateUrl: './suppliers-list.component.html',
  styleUrls: ['./suppliers-list.component.css']
})
export class SuppliersListComponent implements OnInit {


  suppliers?: Supplier[];
  currentSupplier?: Supplier;
  currentIndex = -1;
  title = '';

  constructor(private supplierService: SupplierService) { }

  ngOnInit(): void {
    this.retrieveSuppliers();
  }

  retrieveSuppliers(): void {
    this.supplierService.getAll()
      .subscribe(
        data => {
          this.suppliers = data;
          console.log(data);
        },
        error => {
          console.log(error);
        });
  }

  refreshList(): void {
    this.retrieveSuppliers();
    this.currentSupplier = undefined;
    this.currentIndex = -1;
  }

  setActiveSupplier(supplier: Supplier, index: number): void {
    this.currentSupplier = supplier;
    this.currentIndex = index;
  }

  
}
