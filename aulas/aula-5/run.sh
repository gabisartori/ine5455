rm -rf mutants
echo "Cache removida"
if [ -f tests/test_new.py ]; then
  mv tests/test_new.py{,.bak}
fi
echo "Testes novos ocultados"
echo "Estado atual do projeto:"
tree . -L 2
echo "Executando mutmut"
PYTHONPATH=conteudo:tests mutmut run
echo "Mutantes sobreviventes"
mutmut results | grep -E "(move_tile|get_tile)__mutmut_[0-9]+"
mv tests/test_new.py{.bak,}
echo "Novos Testes para matar os mutantes reativados, estado atual do projeto:"
tree . -L 2
echo "Executando mutmut"
PYTHONPATH=conteudo:tests mutmut run
echo "Mutantes sobreviventes"
mutmut results | grep -E "(move_tile|get_tile)__mutmut_[0-9]+"

