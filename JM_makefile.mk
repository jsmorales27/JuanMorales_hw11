pos.png vel.png phase.png: JM_graph.py tray.txt JM_gravity.cpp
	python JM_graph.py
tray.txt: JM_gravity.cpp
	g++ JM_gravity.cpp
	./a.out>tray.txt
