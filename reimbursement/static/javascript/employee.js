
function openUpdateModal(id, category, expenseType, amount, date, receipt) {
    document.getElementById('updateRequestId').value = id;
    document.getElementById('updateRequestCategory').value = category;
    document.getElementById('updateExpenseType').value = expenseType;
    document.getElementById('updateAmount').value = parseFloat(amount);
    document.getElementById('updateDate').value = date;
    document.getElementById('updateReceipt').dataset.receipt = receipt; 

    // Show the modal
    //creating a  new modal instance for thee updateReimburesmentModal
    var updateModal = new bootstrap.Modal(document.getElementById('updateReimbursementModal'));
    updateModal.show();
}
function changeUpdateAmount(){
    var updateAmountInput = document.getElementById("updateAmount");
    var requestCategory = document.getElementById("updateRequestCategory").value;
    var maxAmount = 0;
    // console.log("change called")
    // console.log(maxAmount)
    if (requestCategory === "Travel") {
        maxAmount = 15000;
    } else if (requestCategory === "Relocation") {      
        maxAmount = 20000;
    } else if (requestCategory === "Tech Assets") {
        maxAmount = 5000;
    }  
    console.log(maxAmount) 
    updateAmountInput.max=maxAmount;
}
function changeExpenseType() {
    var requestCategory = document.getElementById("requestCategory").value;
    var expenseTypeSelect = document.getElementById("expenseType");
    var otherExpenseTypeInput = document.getElementById("otherExpenseType");
    var amountInput = document.getElementById("amount");
    var maxAmount = 0;

    // clearing existing options
    expenseTypeSelect.innerHTML = "";

    // adding options based on request category
    if (requestCategory === "Travel") {
        var travelExpenseTypes = ["Flight", "Hotel", "Meals", "Transportation", "Other"];
        for (var i = 0; i < travelExpenseTypes.length; i++) {
            var option = document.createElement("option");
            option.text = travelExpenseTypes[i];
            option.value = travelExpenseTypes[i];
            expenseTypeSelect.add(option);
        }
        maxAmount = 15000;
    } else if (requestCategory === "Relocation") {
        var relocationExpenseTypes = ["Moving Service", "Temporary Housing", "Storage", "Other"];
        for (var j = 0; j < relocationExpenseTypes.length; j++) {
            var option = document.createElement("option");
            option.text = relocationExpenseTypes[j];
            option.value = relocationExpenseTypes[j];
            expenseTypeSelect.add(option);
        }
        maxAmount = 20000;
    } else if (requestCategory === "Tech Assets") {
        var techAssetExpenseTypes = ["Laptop", "Monitor", "Software", "Accessories", "Other"];
        for (var k = 0; k < techAssetExpenseTypes.length; k++) {
            var option = document.createElement("option");
            option.text = techAssetExpenseTypes[k];
            option.value = techAssetExpenseTypes[k];
            expenseTypeSelect.add(option);
        }
        maxAmount = 5000;
    }

    // updating the max attribute for the amount input field .max is inbuilt
    amountInput.max = maxAmount;
    
    // show/hide Other expense Type input based on selected option
    // if (expenseTypeSelect.value === "Other") {
    //     otherExpenseTypeInput.style.display = "block";
    //     otherExpenseTypeInput.required = true;
    // } else {
    //     otherExpenseTypeInput.style.display = "none";
    //     otherExpenseTypeInput.required = false;
    // }
}

// adding event listener to expense type dropdown
document.getElementById("expenseType").addEventListener("change", function () {
    if (this.value === "Other") {
        document.getElementById("otherExpenseType").style.display = "block";
        document.getElementById("otherExpenseType").required = true;
    } else {
        document.getElementById("otherExpenseType").style.display = "none";
        document.getElementById("otherExpenseType").required = false;
    }
});

document.getElementById("amount").addEventListener("input", function () {
    var maxAmount = parseFloat(this.max);
    var amount = parseFloat(this.value);

    if (amount > maxAmount) {
        this.value = maxAmount; 
        document.getElementById("amountWarning").textContent = "Maximum amount for this expense category is " + maxAmount + ".";
    } else {
        document.getElementById("amountWarning").textContent = "";
    }
});
document.getElementById("updateAmount").addEventListener("input", function () {
    var maxAmount = parseFloat(this.max);
    var amount = parseFloat(this.value);

    if (amount > maxAmount) {
        this.value = maxAmount; 
        document.getElementById("updateAmountWarning").textContent = "Maximum amount for this expense category is " + maxAmount + ".";
    } else {
        document.getElementById("updateAmountWarning").textContent = "";
    }
});

document.addEventListener("DOMContentLoaded", function () {
    var receiptLinks = document.querySelectorAll('.view-receipt');
    receiptLinks.forEach(function (link) {
        link.addEventListener('click', function (event) {
            event.preventDefault(); 

            // get the receipt data from the data attribute
            var receiptData = this.getAttribute('data-receipt');

            // open the receipt image in a new tab
            var newTab = window.open();
            newTab.document.write('<img src="data:image/jpeg;base64,' +
                receiptData + '" style="max-width: 100%; max-height: 100%; display: block; margin: auto;">');

        });
    });
});
