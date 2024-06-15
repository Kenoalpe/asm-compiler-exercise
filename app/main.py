# Internal imports
from app.models import AnalysisModel, SynthesisModel
from app.views import AnalysisView, SynthesisView
from app.controllers import AnalysisController, SynthesisController


def run():
    print('Welcome, let\'s assemble some assembly!\n')

    # Run analysis on the assembly file and return the synthesis_model
    synthesis_model = AnalysisController(model=AnalysisModel('assembler/asm-example.txt'), view=AnalysisView).run()

    # Set the opcode table in the synthesis model
    # synthesis_model.opcode_table = # ToDo Put opcode here
    print(synthesis_model.symbol_table)

    # Run the synthesis to generate machine code
    SynthesisController(model=synthesis_model, view=SynthesisView).run()

