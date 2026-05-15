# 🚀 YOLO Tracking com ROS 2

Este projeto implementa um pipeline de visão computacional utilizando ROS 2, com separação entre aquisição de imagem e processamento com YOLOv8.

---

## 🧠 Arquitetura

O sistema é dividido em dois nós principais:

- 📷 `camera_node` → publica imagens da câmera  
- 🤖 `detector_node` → recebe imagens e executa o modelo YOLO  

---

## 📁 Estrutura do Projeto

```
projeto_ws/
├── src/
│   └── yolo_tracking/
│       ├── yolo_tracking/
│       │   ├── camera_node.py
│       │   ├── detector_node.py
│       │   └── yolov8_tracking.py
│       ├── package.xml
│       ├── setup.py
│       └── setup.cfg
```

---

## ⚙️ Dependências

Instale as dependências necessárias:

```bash
sudo apt update
sudo apt install ros-humble-rviz2
pip install ultralytics opencv-python
```

---

## 🔨 Build do projeto

```bash
cd ~/projeto_ws
colcon build
```

---

## 🔄 Configurar ambiente

```bash
source /opt/ros/humble/setup.bash
source ~/projeto_ws/install/setup.bash
```

---

## ▶️ Como executar

### 🖥️ Terminal 1 — Câmera

```bash
ros2 run yolo_tracking camera_node
```

---

### 🤖 Terminal 2 — Detector YOLO

```bash
ros2 run yolo_tracking detector_node
```

---

## 👀 Visualização no RViz

### 1. Abrir RViz

```bash
rviz2
```

---

### 2. Adicionar display de imagem

- Clique em **Add**
- Selecione **Image**

---

### 3. Configurar

```
Topic: /camera/detection
```

Se necessário:

```
Reliability Policy → Best Effort
```

---

## 🔍 Verificar tópicos

```bash
ros2 topic list
```

Saída esperada:

```
/camera/image_raw
/camera/detection
```

---

## ⚠️ Problemas comuns

### ❌ YOLO não roda

```bash
pip install ultralytics
```

---

### ❌ Câmera não funciona

Verifique dispositivos:

```bash
ls /dev/video*
```

Altere no código se necessário:

```python
cv2.VideoCapture(0)
```

---

### ❌ Nada aparece no RViz

- Verifique se o detector está rodando  
- Ajuste QoS para `Best Effort`  

---

## 🚀 Próximos passos

- Publicar bounding boxes como `Marker`  
- Calcular posição 2D/3D dos objetos  
- Integrar com TF (câmera → mundo)  
- Rodar em múltiplas máquinas (NUC + Jetson)  

---

## 👨‍💻 Autor

Projeto desenvolvido para aplicações em robótica e visão computacional com ROS 2.