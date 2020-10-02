# Perguntas e Tarefas

## mne_obj

1. Nas aulas passadas levantamos a possibilidade de que a identificação dos eventos (marcadores) não estão mapeados para a frequência correta. Utilizando os artifícios do método plot_psd e o ajuste de seus parâmetros, realize diversos plots com diferentes eventos e trials para tentar identificar nos gráficos, o mapeamento correto;

Resposta: Plotamos gráficos com diversos parâmetros (filtros, eventos e trials), não conseguimos identificar com muita clareza se o mapeamento estava correto. Seguimos com o experimento com o mapeamento passado pelo professor.

3 - Falamos em sala de aula que é inviável "chutarmos" quais eletrodos melhor contribuem para nosso experimento quando são muitos! Faça um estudo bibliográfico sobre filtros espaciais em dados EEG. Levante de possíveis algoritmos que podem ser utilizados para discutirmos em aula.

3.1. Quem é o "CAR" dentro do objeto MNE?

Resposta: CAR, Common avarage reference, é uma técnica que pode ser utilizada para fazer a redução de dimensionalidade dos dados, fazendo a diferença entre o potencial de cada eletrodo com a média das somas dos potenciais de todos os eletrodos, reduzindo os potenciais que estão em maior número nos eletrodos. Dentro do MNE, é possível aplicar o CAR com o método `mne.set_eeg_reference`

## preprocessing

1. Como saber quais são os eletrodos a serem utilizados como referência?

Resposta: Faz sentido utilizar os eletrodos que estão alocados na região parietal, ociptal e parieto occipital, pois são referentes e em torno a visão do indivíduo.

2. A média de TODOS os eletrodos é um bom chute?

Resposta: Não, pois muitos dados que não são referentes a visão do indivíduo, podendo trazer ruídos ou apenas dados que poluirão a experiência.

3. Como utilizar as informações de retorno do método set_eeg_reference

Resposta: Foi aplicado o método `set_eeg_reference` diretamente no objeto Epoch, sendo apenas mais uma fase na filtragem espacial.

## features

1. Nem sempre os canais são vistos como características. Uma outra forma é adicionar os canais às amostras (reduzindo a quantidade de características e aumentando a quantidade de amostras). O resultado disso deve ser avaliado.

2. É comum a aplicação de algum algoritmo para reduzir todos os canais ou transformar apenas em um (que é o caso de aplicar a média de todos os eletrodos/canais).

R: Sim, como foi feito e demonstrado, foi adicionado todos os vetores de caracteristicas em uma lista única referênte as extrações da região que está sendo analisada. Essa técnica é utilizada para reduzir e 
simplificar a análise do classificador

3. Adicionar características ruins confundem o resultado? Características que não estão relacionadas ao domínio do problema pode ser ruim? Isso deve ser avaliado...

R: Não necessariamente seja ruim, porém, não faz sentido utilizar características fora do domínio do problema. Ainda mais que num experimento SSVEP, a característica mais "forte" e comum é o PSD. Uma característica que dado os pricípios do SSVEP, faz muito sentido analisar a potência do sinal.