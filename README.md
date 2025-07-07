# 🏦 Sistema de Simulación Bancaria ATM - Dijkstra

Un sistema de simulación bancaria completo que implementa operaciones de cajero automático, transferencias entre cuentas y pagos de servicios utilizando algoritmos de búsqueda y ordenamiento eficientes.

## ✨ Características Principales

- **Gestión de Cuentas**: Registro y autenticación de usuarios
- **Red de Cajeros**: Sistema con 5 cajeros automáticos distribuidos
- **Transferencias**: Sistema completo de transferencias entre cuentas
- **Pagos de Servicios**: Pago a empresas de servicios públicos
- **Gestión de Efectivo**: Manejo de billetes y denominaciones
- **Algoritmos Optimizados**: Implementación de QuickSort y búsqueda binaria

## 🏗️ Arquitectura del Sistema

### Modelos Principales
- **Account**: Gestión de cuentas de usuario
- **Transaction**: Manejo de transferencias entre cuentas
- **ServicePay**: Procesamiento de pagos de servicios
- **ATM**: Control de cajeros automáticos y efectivo
- **Company**: Gestión de empresas de servicios

### Funcionalidades Core
- Sistema de login y registro seguro
- Menú principal interactivo
- Consulta de saldo y historial de transacciones

## 🚀 Instalación y Uso

### Prerrequisitos
- Python 3.x
- Módulos estándar de Python (datetime, random)

### Ejecución
```bash
python ATM/Model/methods.py
```

## 👥 Equipo de Desarrollo

El proyecto fue desarrollado colaborativamente con asignaciones específicas:

- **Yuleisy (A)**: QuickSort, visualización de transacciones, sistema de registro
- **Flavio (B)**: Red de cajeros automáticos, sistema de retiro de efectivo
- **Bruce (C)**: Búsqueda binaria, sistema de login
- **Boyita (D)**: Lógica de transferencias, pagos de servicios
- **Jesús (E)**: Manejo genérico de efectivo

## 🔧 Funcionalidades Técnicas

### Algoritmos Implementados
- **QuickSort**: Para ordenamiento eficiente de listas de cuentas
- **Búsqueda Binaria**: Para localización rápida de cuentas por DNI, email o teléfono

### Gestión de Datos
- Búsqueda multi-criterio de cuentas
- Búsqueda de empresas por RUC
- Manejo automático de inventario de billetes

## 💰 Operaciones Bancarias

### Transferencias
- Validación de saldo suficiente
- Actualización automática de balances
- Registro completo de transacciones

### Pagos de Servicios
Empresas soportadas:
- Internet
- Electricidad  
- Agua potable
- Gas natural
- Telefonía

### Gestión de Efectivo
- Retiro con validación de disponibilidad
- Conteo automático de billetes por denominación
- Actualización de inventario en tiempo real

## 📝 Estado del Proyecto

Este es un proyecto educativo que demuestra la implementación de:
- Estructuras de datos eficientes
- Algoritmos de búsqueda y ordenamiento
- Arquitectura de software modular
- Simulación de sistemas bancarios reales

## 🤝 Contribuciones

El proyecto sigue un modelo de desarrollo colaborativo con tareas específicamente asignadas. Para contribuir, revisa las especificaciones técnicas en el código fuente.

---

*Desarrollado como proyecto académico para demostrar conceptos de algoritmos y estructuras de datos aplicados a sistemas bancarios.*
