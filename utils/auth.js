import Cookies from "js-cookie";

export function isAuthenticated() {
    const token = getAuthToken();
    console.log(token) 
    if (token == undefined) {
      return false
    } else {
      return true
    }
  }
  
  // Obtener el token de las cookies o almacenamiento local
  export function getAuthToken() {
    return Cookies.get('token');
  }
  