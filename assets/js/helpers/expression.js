export const expressionReg = {
    email: /^[^\s@]+@[^\s@]+\.[^\s@]+$/,
    password: /^(?=.*[A-Z])(?=.*\d)(?=.*[\W_]).{8,}$/,
    text: /^[A-Za-z ]{4,}$/,
    number: /^\d/
}
