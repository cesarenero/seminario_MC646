describe('Página do Google', () => {
  it('deve exibir o título correto', () => {
    cy.visit('https://www.google.com')

    // Espera até que o título da página contenha "Google"
    cy.title().should('include', 'Google')
  })
})
