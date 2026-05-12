use crate::project::Project;
use crate::employee::Employee;

pub struct Company {
  name: String,
  id: usize,
  employees: Vec<Employee>,
  projects: Vec<Project>
}