function confirmarDelete(id) {
    Swal.fire({
        title: "Estás seguro?",
        text: "Esta acción no se puede revertir!",
        icon: "error",
        showCancelButton: true,
        confirmButtonColor: "#3085d6",
        cancelButtonColor: "#d33",
        confirmButtonText: "Si, eliminar!"
      }).then((result) => {
        if (result.isConfirmed) {
          Swal.fire({
            title: "Eliminado!",
            text: "Empleado eliminado correctamente.",
            icon: "success"
          }).then(function() {
            window.location.href = "delete/" + id + "/";
          })
        }
      });
}