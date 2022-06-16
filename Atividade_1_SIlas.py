maxpont001=[1,]
maxpont002=[1,]
maxpont003=[1,]
maxpont004=[1,]
maxpont005=[1,]
maxpont006=[1,]
maxpont007=[1,]
totaldecand=0
totaldecandap=0
iscrit001=[]
iscrit002=[]
iscrit003=[]
iscrit004=[]
iscrit005=[]
iscrit006=[]
iscrit007=[]
idad=int(input('Digite sua idade:'))
while idad<30 or idad>120:
  print('Cadastro impossibilitado')
  idad=int(input('Digite sua idade:'))
while idad>=30 and idad<=120:
        cdi=str(input('Digite seu codigo de inscrição:'))
        print('Cadastro permitido')
        soma=0
        totaldecand=totaldecand+1
        casa=str(input('Digite o nome da casa que você pertence(Grifinória,Sonserina,Lufa-Lufa ou Corvinal):'))
        if casa=='Grifinória':
                soma=soma+20
        elif casa=='Sonserina':
                soma=soma+10
        elif casa=='Lufa-Lufa':
                soma=soma+15
        elif casa=='Corvinal':
                soma=soma+15
        print('------------------------------------------------------------------------------------')
        especialidade=str(input('Qual a sua especialidade?(Herbologia,Poções,Defesa contra as artes das trevas,Transfiguração,História da magia ou Feitiços)'))
        if especialidade=='Herbologia':
                soma=soma+10
        elif especialidade=='Poções':
                soma=soma+15
        elif especialidade=='Defesa contra as artes das trevas':
                soma=soma+25
        elif especialidade=='Transfiguração':
                soma=soma+20
        elif especialidade=='História da magia':
                soma=soma+10
        elif especialidade=='Feitiços':
                soma=soma+25
        print('------------------------------------------------------------------------------------')
        print('Responda as perguntas com (S)para sim e (N)para não')
        time=str(input('Você faz parte de um time de quadribol?'))
        if time=='S':
                soma=soma+10
        sangue=str(input('Você é um bruxo(a) sangue-puro?'))
        if sangue=='S':
                soma=soma+15
        print('Hermione repreende totalmente qualquer exploração aos elfos, sendo assim, caso o bruxo tenha um elfo doméstico, ele perde 20 pontos!')
        elfo=str(input('Você tem um elfo?'))
        if elfo=='S':
                soma=soma-20
        print('O Patrono é imprescindível na luta contra os dementadores, sendo assim, ter despertado o próprio patrono é um ponto positivo, garantindo +15 pontos!')
        patrono=str(input('Você despertou seu próprio patrono?'))
        if patrono=='S':
                soma=soma+15
        print('Sua nota é',soma)
        totaldecandap=0
        print('------------------------------------------------------------------------------------')
        print('Lista de Departamentos para insçrição')
        print('Departamento de Execução das Leis da Magia:001')
        print('Departamento de Acidentes e Catástrofes Mágicas:002')
        print('Departamento para Regulamentação e Controle das Criaturas Mágicas:003')
        print('Departamento de Cooperação Internacional em Magia:004')
        print('Departamento de Transportes Mágicos:005')
        print('Departamento de Jogos e Esportes Mágicos:006')
        print('Departamento de Mistérios:007')
        cddp=str(input('Digite o código do departamento que dejesa:'))
        if cddp=='001':
                iscrit001.append(soma)
                if soma>45:
                    totaldecandap=totaldecandap+1
                    if soma>=45 and soma>max(maxpont001):
                        print('Aprovado')
                        maxpont001.append(soma)
                        cdmai001=cdi
                    elif soma>=45 and soma==max(maxpont001):
                        print('Candidato reprovado')
                else:
                    print('Candidato reprovado')
        if cddp=='002':
                iscrit002.append(soma)
                if soma>45:
                    totaldecandap=totaldecandap+1
                    if soma>=45 and soma>max(maxpont002):
                        print('Aprovado')
                        maxpont002.append(soma)
                        cdmai002=cdi
                    elif soma>=45 and soma==max(maxpont002):
                        print('Candidato reprovado')
                else:
                    print('Candidato reprovado')
        if cddp=='003':
                iscrit003.append(soma)
                if soma>45:
                    totaldecandap=totaldecandap+1
                    if soma>=45 and soma>max(maxpont003):
                        print('Aprovado')
                        maxpont003.append(soma)
                        cdmai003=cdi
                    elif soma>=45 and soma==max(maxpont003):
                        print('Candidato reprovado')
                else:
                    print('Candidato reprovado')
        if cddp=='004':
                iscrit004.append(soma)
                if soma>45:
                    totaldecandap=totaldecandap+1
                    if soma>=45 and soma>max(maxpont004):
                        print('Aprovado')
                        maxpont004.append(soma)
                        cdmai004=cdi
                    elif soma>=45 and soma==max(maxpont004):
                        print('Candidato reprovado')
                else:
                    print('Candidato reprovado')
        if cddp=='005':
                iscrit005.append(soma)
                if soma>45:
                    totaldecandap=totaldecandap+1
                    if soma>=45 and soma>max(maxpont005):
                        print('Aprovado')
                        maxpont005.append(soma)
                        cdmai005=cdi
                    elif soma>=45 and soma==max(maxpont005):
                        print('Candidato reprovado')
                else:
                    print('Candidato reprovado')
        if cddp=='006':
                iscrit006.append(soma)
                if soma>45:
                    totaldecandap=totaldecandap+1
                    if soma>=45 and soma>max(maxpont006):
                        print('Aprovado')
                        maxpont006.append(soma)
                        cdmai006=cdi
                    elif soma>=45 and soma==max(maxpont006):
                        print('Candidato reprovado')
                else:
                    print('Candidato reprovado')
        if cddp=='007':
                iscrit007.append(soma)
                if soma>45:
                    totaldecandap=totaldecandap+1
                    if soma>=45 and soma>max(maxpont007):
                        print('Aprovado')
                        maxpont007.append(soma)
                        cdmai007=cdi
                    elif soma>=45 and soma==max(maxpont007):
                        print('Candidato reprovado')
                else:
                    print('Candidato reprovado')
        idad=int(input('Digite sua idade(ou uma idade negativa para obter resultados):'))
else:
  if idad<=1:
    print('O total de candidatos inscritos é',totaldecand)
    print('------------------------------------------------------------------------------------')
    if (totaldecand>0):
        pdca=totaldecandap*100/totaldecand
        print('O total de candidatos aptos é {}%'.format(pdca))
    print('------------------------------------------------------------------------------------')
    print('O total de inscritos para o Departamento de Execução das Leis da Magia é:',len(iscrit001))
    print('O total de inscritos para o Departamento de Acidentes e Catástrofes Mágicas é:',len(iscrit002))
    print('O total de inscritos para o Departamento para Regulamentação e Controle das Criaturas Mágicas é:',len(iscrit003))
    print('O total de inscritos para o Departamento de Cooperação Internacional em Magia é',len(iscrit004))
    print('O total de inscritos para o Departamento de Transportes Mágicos é:',len(iscrit005))
    print('O total de inscritos para o Departamento de Jogos e Esportes Mágicos é:',len(iscrit006))
    print('O total de inscritos para o Departamento de Mistérios é:',len(iscrit007))
    print('------------------------------------------------------------------------------------')
    if len(iscrit001)>0:
                print('O pior candidato inscrito para o Departamento de Execução das Leis da Magia tem nota',min(iscrit001))
    else:
                print('Nenhum candidato inscrito para o Departamento de Execução das Leis da Magia')
    if len(iscrit002)>0:
                print('O pior candidato inscrito para o Departamento de Acidentes e Catástrofes Mágicas tem nota',min(iscrit002))
    else:
                print('Nenhum candidato inscrito para o Departamento de Acidentes e Catástrofes Mágicas')
    if len(iscrit003)>0:
                print('O pior candidato inscrito para o Departamento para Regulamentação e Controle das Criaturas Mágicas',min(iscrit003))
    else:
                print('Nenhum candidato inscrito para o Departamento para Regulamentação e Controle das Criaturas Mágicas')
    if len(iscrit004)>0:
                print('O pior candidato inscrito para o Departamento de Cooperação Internacional em Magia tem nota',min(iscrit004))
    else:
                print('Nenhum candidato inscrito para o Departamento de Cooperação Internacional em Magia')
    if len(iscrit005)>0:
                print('O pior candidato inscrito para o Departamento de Transportes Mágicos é tem nota',min(iscrit005))
    else:
                print('Nenhum candidato inscrito para o Departamento de Transportes Mágicos é')
    if len(iscrit006)>0:
                print('O pior candidato inscrito para o Departamento de Jogos e Esportes Mágicos tem nota',min(iscrit006))
    else:
                print('Nenhum candidato inscrito para o Departamento de Jogos e Esportes Mágicos é')
    if len(iscrit007)>0:
                print('O pior candidato inscrito para o Departamento de Mistérios  tem nota',min(iscrit007))
    else:
                print('Nenhum candidato inscrito para o Departamento de Mistérios ')
    print('------------------------------------------------------------------------------------')
    if len(maxpont001)>=2:
            print('O candidato aprovado para o Departamento de Execução das Leis da Magia tem nota',max(maxpont001))
            print('Codigo do aprovado',cdmai001)
    else:
            print('Nenhum candidato aprovado para o Departamento de Execução das Leis da Magia')
    if len(maxpont002)>=2:
            print('O candidato aprovado para o Departamento de Acidentes e Catástrofes Mágicas tem nota',max(maxpont002))
            print('Codigo do aprovado',cdmai002)
    else:
            print('Nenhum candidato aprovado para o Departamento de Acidentes e Catástrofes Mágicas')
    if len(maxpont003)>=2:
            print('O  candidato aprovado para o Departamento para Regulamentação e Controle das Criaturas Mágicas',max(maxpont003))
            print('Codigo do aprovado',cdmai003)
    else:
            print('Nenhum candidato aprovado para o Departamento para Regulamentação e Controle das Criaturas Mágicas')
    if len(maxpont004)>=2:
            print('O  candidato aprovado para o Departamento de Cooperação Internacional em Magia tem nota',max(maxpont004))
            print('Codigo do aprovado',cdmai004)
    else:
            print('Nenhum candidato aprovado para o Departamento de Cooperação Internacional em Magia')
    if len(maxpont005)>=2:
            print('O  candidato aprovado para o Departamento de Transportes Mágicos é tem nota',max(maxpont005))
            print('Codigo do aprovado',cdmai005)
    else:
            print('Nenhum candidato aprovado para o Departamento de Transportes Mágicos é')
    if len(maxpont006)>=2:
            print('O candidato aprovado para o Departamento de Jogos e Esportes Mágicos tem nota',max(maxpont006))
            print('Codigo do aprovado',cdmai006)
    else:
            print('Nenhum candidato aprovado para o Departamento de Jogos e Esportes Mágicos é')
    if len(maxpont007)>=2:
            print('O  candidato aprovado para o Departamento de Mistérios  tem nota',max(maxpont007))
            print('Codigo do aprovado',cdmai007)
    else:
            print('Nenhum candidato aprovado para o Departamento de Mistérios')

