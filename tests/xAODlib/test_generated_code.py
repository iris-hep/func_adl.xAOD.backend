# Test the generated code object
from func_adl.xAOD.backend.xAODlib.generated_code import generated_code
import func_adl.xAOD.backend.xAODlib.statement as statement

class dummy_emitter:
    def __init__ (self):
        self.Lines = []

    def add_line (self, l):
        self.Lines += [l]

    def process (self, func):
        func(self)
        return self

def test_nothing():
    g = generated_code()
    assert 0 == len(g.class_declaration_code())
    assert 2 == len(dummy_emitter().process(g.emit_query_code).Lines)

def test_insert_two_levels():
    s1 = statement.iftest("true")
    s2 = statement.set_var("v1", "true")
    g = generated_code()

    g.add_statement(s1)
    g.add_statement(s2)

    assert 1 == len(s1._statements)

def test_insert_in_middle():
    s1 = statement.iftest("true")
    s2 = statement.set_var("v1", "true")
    g = generated_code()

    g.add_statement(s1)
    g.add_statement(s2)

    s3 = statement.iftest("fork")
    g.add_statement(s3, below=s1)

    assert 1 == len(s1._statements)
    assert 1 == len(s3._statements)

    assert s1._statements[0] is s3
    assert s3._statements[0] is s2

def test_get_rep_null():
    g = generated_code()
    assert None is g.get_rep("hi")

def test_get_rep_when_set():
    g = generated_code()
    g.set_rep("dude", 5)
    assert 5 is g.get_rep("dude")

def test_get_rep_when_set_level_up():
    g = generated_code()
    g.set_rep("dude", 5)
    s1 = statement.iftest("true")
    g.add_statement(s1)
    assert 5 is g.get_rep("dude")

def test_get_rep_works_and_doesnt():
    g = generated_code()
    s1 = statement.iftest("true")
    g.set_rep("dude", 5)
    assert 5 is g.get_rep("dude")
    g.pop_scope()
    assert None is g.get_rep("dude")

def test_get_rep_hidden():
    g = generated_code()
    g.set_rep("dude", 5)
    s1 = statement.iftest("true")
    g.add_statement(s1)
    g.set_rep("dude", 10)
    assert 10 is g.get_rep("dude")
    g.pop_scope()
    assert 5 is g.get_rep("dude")
