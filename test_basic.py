
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Teste básico do sistema ARQV30 Enhanced
"""

import os
import sys
import traceback

def test_imports():
    """Testa imports básicos"""
    print("🧪 Testando imports...")
    
    try:
        import flask
        print("✅ Flask")
        
        import requests
        print("✅ Requests")
        
        # Adiciona src ao path
        sys.path.insert(0, 'src')
        
        from services.environment_loader import environment_loader
        print("✅ Environment Loader")
        
        print("✅ Todos os imports básicos funcionando!")
        return True
        
    except Exception as e:
        print(f"❌ Erro no import: {e}")
        traceback.print_exc()
        return False

def test_environment():
    """Testa configuração de ambiente"""
    print("\n🔧 Testando ambiente...")
    
    try:
        from services.environment_loader import environment_loader
        validation = environment_loader.validate_environment()
        
        if validation['valid']:
            print("✅ Ambiente configurado corretamente")
        else:
            print(f"⚠️ Variáveis ausentes: {validation['missing']}")
            print("📝 Configure o arquivo .env baseado no .env.example")
        
        return True
        
    except Exception as e:
        print(f"❌ Erro na validação: {e}")
        return False

def test_directories():
    """Testa criação de diretórios"""
    print("\n📁 Testando diretórios...")
    
    directories = [
        'logs',
        'src/uploads', 
        'src/static/images'
    ]
    
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        print(f"✅ {directory}")
    
    return True

def main():
    """Executa testes básicos"""
    print("=" * 60)
    print("🚀 TESTE BÁSICO - ARQV30 Enhanced v2.0")
    print("=" * 60)
    
    tests = [
        ("Imports", test_imports),
        ("Ambiente", test_environment), 
        ("Diretórios", test_directories)
    ]
    
    results = []
    
    for test_name, test_func in tests:
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"❌ Erro em {test_name}: {e}")
            results.append((test_name, False))
    
    # Relatório final
    print("\n" + "=" * 60)
    print("📊 RELATÓRIO DE TESTES")
    print("=" * 60)
    
    passed = 0
    for test_name, result in results:
        status = "✅ PASSOU" if result else "❌ FALHOU"
        print(f"{test_name:.<30} {status}")
        if result:
            passed += 1
    
    print(f"\nTotal: {passed}/{len(results)} testes passaram")
    
    if passed == len(results):
        print("\n🎉 SISTEMA BÁSICO FUNCIONANDO!")
        print("Execute: python src/run.py")
    else:
        print("\n⚠️ Alguns testes falharam")
        print("Verifique os erros acima")

if __name__ == '__main__':
    main()
