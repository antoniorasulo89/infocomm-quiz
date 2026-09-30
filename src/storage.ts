const prefix='infocomm-v2-';
export let storageAvailable=true;
export function read<T>(key:string,fallback:T):T{try{return JSON.parse(localStorage.getItem(prefix+key)||'null')??fallback;}catch{return fallback;}}
export function write(key:string,value:unknown){try{localStorage.setItem(prefix+key,JSON.stringify(value));return true;}catch{storageAvailable=false;return false;}}
export function remove(key:string){try{localStorage.removeItem(prefix+key);}catch{storageAvailable=false;}}
