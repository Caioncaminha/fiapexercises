// Class called "Produto" with the following attributes:
// name (string)
// price (double)
// quantity (int)

// Implement the following methods:
// exibitInformation(): void - displays the product's information
// calculateTotalValue(): double - calculates the total value of the product (price * quantity)

public class Produto {
    public String name;
    public double price;
    public int quantity;
    
// Constructor
    public Produto(String name, double price, int quantity) {
        this.name = name;
        this.price = price;
        this.quantity = quantity;
    }
    
    // Method to display product information
    public void exibitInformation() {
        System.out.println("Product: " + name);
        System.out.println("Price: $" + price);
        System.out.println("Quantity: " + quantity);
    }

    // Method to calculate total value of the product
    public double calculateTotalValue() {
        return price * quantity;
    }
}

