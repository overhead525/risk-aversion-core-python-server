# risk-aversion-core-python-server
A server allowing the use of the core simulation executable. Exposed through a GraphQL API.

The purpose of this server is solely to run and simulations based on parameters, and to store those simulations based on generated unique identifiers.
A PostgreSQL database, hosted using AWS Relational Database, will be used for storage. Note: All simulations are stored agnostically, meaning this
server has no idea which simulations were run by which individual, for security reasons.

Example GraphQL Request

```
// Run a simulation
mutation {
  simulate (
    principal: 100000,
    riskDecimal: 0.01,
    rewardDecimal: 0.03,
    winDecimal: 0.55,
    lossDecimal: 0.45,
    breakEvenDecimal: 0.25,
    numOfTrades: 50,
    numOfSimulations: 100
  ) {
    result {
      maxPortfolio
      minPortfolio
    }
  }
}
```

Expected Result

```
{
  simID: 8dk2-29dj-d8l2-8dj2,
  maxPortfolio: 645023.77,
  minPortfolio: 56934.23
}
```
