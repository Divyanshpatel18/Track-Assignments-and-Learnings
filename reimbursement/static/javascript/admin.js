// The function is built to redirect form submission accordingly to different actions like approve or reject
    function setAction(action, form) {
        if (action === 'approve') {
            form.action = '/approve_reimbursement';
        } else if (action === 'reject') {
            form.action = '/reject_reimbursement';
        }
        // Submit the form
        form.submit();
    }
    //  for dynamically setting progress bar widths
    // the  arguments are being passed form app.py
    var totalUsers = "{{ total_users }}";
    var maxUsers = "{{ max_users }}";
    var progressWidthUsers = (totalUsers / maxUsers) * 100;
    document.getElementById("progressUsers").style.width = progressWidthUsers + "%";

    var totalDepartments = "{{ total_departments }}";
    var maxDepartments ="{{ max_departments }}";
    var progressWidthDepartments = (totalDepartments / maxDepartments) * 100;
    document.getElementById("progressDepartments").style.width = progressWidthDepartments + "%";

    var totalApprovedRejected = "{{ total_approved_rejected_reimbursements }}";
    var maxApprovedRejected = "{{ max_approved_rejected_reimbursements }}";
    var progressWidthApprovedRejected = (totalApprovedRejected / maxApprovedRejected) * 100;
    document.getElementById("progressApprovedRejected").style.width = progressWidthApprovedRejected + "%";

    var totalPending = "{{ total_pending_reimbursements }}";
    var maxPending = "{{ max_pending_reimbursements }}";
    var progressWidthPending = (totalPending / maxPending) * 100;
    document.getElementById("progressPending").style.width = progressWidthPending + "%";

    document.addEventListener("DOMContentLoaded", function() {
        var receiptLinks = document.querySelectorAll('.view-receipt');
        receiptLinks.forEach(function(link) {
            link.addEventListener('click', function(event) {
                event.preventDefault(); // prevent default anchor behavior

                // getting receipt data from the data attribute
                var receiptData = this.getAttribute('data-receipt');

                // to open the receipt image in a new tab
                var newTab = window.open();
                newTab.document.write('<img src="data:image/jpeg;base64,' +
                receiptData + '" style="max-width: 100%; max-height: 100%; display: block; margin: auto;">');

            });
        });
    });