function openTab(evt, tabName) {
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tablink");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
    document.getElementById(tabName).style.display = "block";
    evt.currentTarget.className += " active";
}

function toggleMenu() {
    var x = document.getElementsByClassName("tabs")[0];
    if (x.style.display === "block") {
        x.style.display = "none";
    } else {
        x.style.display = "block";
    }
}

document.getElementById("AddExpense").style.display = "block";
document.querySelector(".tablink").className += " active";

// Встановлення сьогоднішньої дати за замовчуванням
document.getElementById('date').valueAsDate = new Date();

function confirmDelete(type, id) {
    var modal = document.getElementById('confirmDeleteModal');
    var deleteButton = document.getElementById('confirmDeleteButton');
    document.getElementById('deleteType').innerText = type;
    modal.style.display = "block";
    deleteButton.onclick = function() {
        window.location.href = `/delete_${type}/${id}`;
    }
}

function closeModal(modalId) {
    var modal = document.getElementById(modalId);
    modal.style.display = "none";
}

function editCategory(id, name) {
    var modal = document.getElementById('editCategoryModal');
    document.getElementById('editCategoryName').value = name;
    document.getElementById('editCategoryId').value = id;
    modal.style.display = "block";
    document.getElementById('editCategoryForm').action = `/edit_category/${id}`;
}

function editExpense(id, amount, categoryId, comment, date) {
    var modal = document.getElementById('editExpenseModal');
    document.getElementById('editExpenseAmount').value = amount;
    document.getElementById('editExpenseCategory').value = categoryId;
    document.getElementById('editExpenseComment').value = comment;
    document.getElementById('editExpenseDate').value = date;
    document.getElementById('editExpenseId').value = id;
    modal.style.display = "block";
    document.getElementById('editExpenseForm').action = `/edit_expense/${id}`;
}

// Додатковий код для повернення до вигляду ПК
function adjustMenuVisibility() {
    var menuButton = document.getElementsByClassName('menu-button')[0];
    var tabs = document.getElementsByClassName('tabs')[0];
    if (window.innerWidth > 600) {
        menuButton.style.display = 'none';
        tabs.style.display = 'flex';
    } else {
        menuButton.style.display = 'block';
        tabs.style.display = 'none';
    }
}

// Виконати adjustMenuVisibility при завантаженні сторінки
window.addEventListener('load', adjustMenuVisibility);

// Виконати adjustMenuVisibility при зміні розміру вікна
window.addEventListener('resize', adjustMenuVisibility);