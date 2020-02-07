// Erstellung des AST

pub fn run() {
    let mut n = Node::new("test".to_string());
    println!("n: {:?}", n);
    let mut c = Node::new("test2".to_string());
    let c2 = Node::new("test3".to_string());

    n.push_child(c);
    println!("n:  {:?}", n);
    let mut cu = n.find_child("test2").unwrap();
    cu.push_child(c2);
    println!("{:?}", n);
}

enum Token {
}

#[derive(Debug)]
struct Node {
    op: String,
    child: Vec::<Node>,
}

impl Node {
    fn new(op: String) -> Node {
        Node {
            op,
            child: Vec::new(),
        }
    }
    fn push_child(&mut self, child: Node) {
        self.child.push(child);
    }
    fn find_child(&mut self, op: &str) -> Option<&mut Node> {
        let mut index: Option<usize> = None;
        for i in 0..self.child.len() {
            if self.child[i].return_op() == op {
                index = Some(i);
            }
        }
        match index {
            Some(i) => Some(&mut self.child[i]),
            None => None,
        }
    }
    fn return_op(&self) -> &str {
        &self.op
    }
}