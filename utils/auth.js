import axios from "axios";
import Cookies from "js-cookie";

export function isAuthenticated() {
    const token = getAuthToken(); 
    if (token == undefined) {
      return false
    } else {
      return true
    }
  }

 export async function validateGroup() {
    const svg = Cookies.get('svg')
    let result = null;
    await axios.get(`http://127.0.0.1:8000/api/users/${svg}`, {
      headers: {
        Authorization: `Token ${Cookies.get('token')}`
      }
    })
    .then(response => {
      result = response.data.group
    })
    return result
  }

  
  // Obtener el token de las cookies o almacenamiento local
  export function getAuthToken() {
    return Cookies.get('token');
  }
  