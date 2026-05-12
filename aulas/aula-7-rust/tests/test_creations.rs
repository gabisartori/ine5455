use crate::src::company::Company;

#[cfg(test)]
mod tests {
  use super::*;
  
  #[test]
  pub fn test_company_creation() {
    let company: Company = Company::new();
  }
}